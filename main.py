from simulation import Simulation


if __name__ == '__main__':
    sim = Simulation(num_sheep=15, max_rounds=50, sheep_move_dist=0.5, wolf_move_dist=1.0,
                     init_pos_limit=10.0, wolf_x=0.0, wolf_y=0.0)
    sim.run()