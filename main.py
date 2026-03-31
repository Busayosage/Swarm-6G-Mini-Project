from experiments import run_experiments
from visualization import VisualSwarmSimulation


def main():
    print("\nSwarm-6G Mini Project")
    print("----------------------")
    print("1 - Run experiments")
    print("2 - Run visualization")
    print("3 - Exit")

    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == "1":
        print("\nRunning experiments...\n")
        run_experiments()
        print("\nExperiments complete.")

    elif choice == "2":
        print("\nStarting visualization...\n")
        sim = VisualSwarmSimulation(
            num_agents=15,
            width=100,
            height=100,
            communication_radius=20,
            latency_steps=3,
            packet_loss=0.2,
            target=(80, 80),
            target_radius=8,
            seed=1
        )
        sim.run(steps=120)
        print("\nVisualization finished.")

    elif choice == "3":
        print("\nExiting project.")

    else:
        print("\nInvalid choice. Please run the program again and enter 1, 2, or 3.")


if __name__ == "__main__":
    main()