import os
import pandas as pd
import matplotlib.pyplot as plt

from simulation import SwarmSimulation


def run_experiments():
    scenarios = [
        {"name": "baseline", "latency_steps": 0, "packet_loss": 0.0},
        {"name": "high_latency", "latency_steps": 8, "packet_loss": 0.0},
        {"name": "high_packet_loss", "latency_steps": 0, "packet_loss": 0.5},
        {"name": "combined_constraints", "latency_steps": 8, "packet_loss": 0.5},
    ]

    seeds = [1, 2, 3, 4, 5]
    all_results = []

    for scenario in scenarios:
        for seed in seeds:
            sim = SwarmSimulation(
                num_agents=15,
                width=100,
                height=100,
                steps=250,
                communication_radius=20,
                latency_steps=scenario["latency_steps"],
                packet_loss=scenario["packet_loss"],
                target=(80, 80),
                target_radius=8,
                seed=seed
            )

            result = sim.run()
            result["scenario"] = scenario["name"]
            result["seed"] = seed
            result["latency_steps"] = scenario["latency_steps"]
            result["packet_loss"] = scenario["packet_loss"]
            all_results.append(result)

    df = pd.DataFrame(all_results)

    os.makedirs("results", exist_ok=True)

    csv_path = "results/experiment_results.csv"
    df.to_csv(csv_path, index=False)

    summary = df.groupby("scenario").agg({
        "coverage": ["mean", "std"],
        "time_to_complete": ["mean", "std"],
        "coordination_efficiency": ["mean", "std"],
        "signals_received_agents": ["mean", "std"],
        "messages_sent": ["mean", "std"],
        "messages_delivered": ["mean", "std"],
        "messages_dropped": ["mean", "std"]
    })

    print("\n=== EXPERIMENT SUMMARY ===")
    print(summary)

    plot_bar_means(df, "coverage", "Coverage by Scenario", "results/coverage_plot.png")
    plot_bar_means(df, "time_to_complete", "Time to Complete by Scenario", "results/time_plot.png")
    plot_bar_means(df, "coordination_efficiency", "Coordination Efficiency by Scenario", "results/coordination_plot.png")
    plot_bar_means(df, "signals_received_agents", "Agents Receiving Signals by Scenario", "results/signals_plot.png")

    print(f"\nCSV saved to: {csv_path}")
    print("Plots saved in: results/")

    return df


def plot_bar_means(df, metric_name, title, save_path):
    grouped = df.groupby("scenario")[metric_name]
    means = grouped.mean()
    stds = grouped.std()

    plt.figure(figsize=(8, 5))
    means.plot(kind="bar", yerr=stds, capsize=4)
    plt.title(title)
    plt.ylabel(metric_name)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()