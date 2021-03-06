#!/usr/bin/env python

import os
import autodisc as ad

def run_animal_exploration():
    # define exploration parameters

    directory = os.path.join(os.path.dirname(__file__), "results_animal_exploration")

    system_parameters = ad.systems.Lenia.default_system_parameters()
    system_parameters.size_y = 256
    system_parameters.size_x = 256

    lenia = ad.systems.Lenia(system_parameters=system_parameters)


    animal_explorer = ad.systems.lenia.LeniaAnimalExplorer(system=lenia)
    animal_explorer.data.config.save_automatic = True
    animal_explorer.data.config.keep_saved_runs_in_memory = True
    animal_explorer.data.config.keep_saved_observations_in_memory = False
    animal_explorer.data.config.directory = directory

    # run exploration
    animal_explorer.run(animal_ids=range(10), verbose=True)
    #animal_explorer.run(verbose=True)
    animal_explorer.save()

    return animal_explorer


def view_exploration_results(animal_explorer):

    gui_config = ad.gui.ExplorationGUI.default_gui_config()

    gui_config['max_num_of_obs_in_memory'] = 20
    gui_config['experiment_num_of_steps'] = 300

    gui_config['statistic_columns'] = []
    gui_config['statistic_columns'].append({'stat_name': 'activation_mass_mean', 'disp_name': 'act mass', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'positive_growth_mass_mean', 'disp_name': 'growth mass', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_volume_mean', 'disp_name': 'act volume', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'positive_growth_volume_mean', 'disp_name': 'growth volume', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_density_mean', 'disp_name': 'act density', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'positive_growth_density_mean', 'disp_name': 'growth density', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_center_velocity_mean', 'disp_name': 'act centroid speed', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_positive_growth_centroid_distance_mean', 'disp_name': 'act-growth centroid distance', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_center_movement_angle_velocity_mean', 'disp_name': 'act centroid rotate speed', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'positive_growth_center_movement_angle_velocity_mean', 'disp_name': 'growth centroid rotate speed', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_hu1_mean', 'disp_name': 'act hu 1', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_hu4_mean', 'disp_name': 'act hu 4', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_hu5_mean', 'disp_name': 'act hu 5', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_hu6_mean', 'disp_name': 'act hu 6', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_hu7_mean', 'disp_name': 'act hu 7', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_hu8_mean', 'disp_name': 'act hu 8', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_flusser9_mean', 'disp_name': 'act flusser 9', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_flusser10_mean', 'disp_name': 'act flusser 10', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_flusser11_mean', 'disp_name': 'act flusser 11', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_flusser12_mean', 'disp_name': 'act flusser 12', 'format': '{:.3f}'})
    gui_config['statistic_columns'].append({'stat_name': 'activation_flusser13_mean', 'disp_name': 'act flusser 13', 'format': '{:.3f}'})

    gui_config['detail_views'].append({'gui': 'autodisc.gui.ExplorationParametersGUI',
                                       'gui_config': {'run_parameters_config': [{'type': 'table', 'parameters': 'all'},
                                                                                {'type': 'image', 'parameters': [{'name': 'init_state'}], 'gui_config': {'pixel_size': 1}}]
                                                     }})

    gui_config['detail_views'].append({'gui': 'autodisc.gui.ObservationPlayerGUI',
                                      'gui_config': {'pixel_size': 2,
                                                     'elements': [{'type': 'arrow_angle',
                                                                   'is_visible': True,
                                                                   'position': {'source': 'statistics',
                                                                                'name': 'activation_center_position'},
                                                                   'length': {'source': 'statistics',
                                                                              'name': 'activation_center_velocity',
                                                                              'factor': 20},
                                                                   'angle': {'source': 'statistics',
                                                                              'name': 'activation_center_movement_angle'}
                                                                   },
                                                                  {'type': 'arrow_angle',
                                                                   'is_visible': False,
                                                                   'position': {'source': 'statistics',
                                                                                'name': 'positive_growth_center_position'},
                                                                   'length': {'source': 'statistics',
                                                                              'name': 'positive_growth_center_velocity',
                                                                              'factor': 20},
                                                                   'angle': {'source': 'statistics',
                                                                             'name': 'positive_growth_center_movement_angle'}
                                                                   }
                                                                  ]
                                                     }
                                      })

    gui_config['detail_views'].append({'gui': 'autodisc.gui.ObservationPreviewGUI',
                                       'gui_config': {'pixel_size': 1, 'steps': [[0, 10, 20, 30, 40],
                                                                                 [50, 1 / 4, 1 / 2, 3 / 4, -1]]}
                                      })

    gui_config['detail_views'].append({'gui': 'autodisc.gui.StatisticTableGUI',
                                       'gui_config': {'statistics': [{'name': 'activation_mass_mean', 'disp_name': 'activation (mean)', 'format': '{:.3f}'},
                                                                     {'name': 'activation_mass_std', 'disp_name': 'activation (std)', 'format': '{:.3f}'}]
                                                     }})

    gui_config['detail_views'].append({'gui': 'autodisc.gui.StatisticLineGUI',
                                       'gui_config': {'statistics': [{'name': 'activation_mass', 'disp_name': 'activation mass'},
                                                                     {'name': 'positive_growth_mass', 'disp_name': 'positive growth mass'}]
                                                     }})

    gui_config['detail_views'].append({'gui': 'autodisc.gui.StatisticBarGUI',
                                       'gui_config': {'statistics': [{'name': 'activation_mass_mean', 'disp_name': 'activation mass (mean)'},
                                                                     {'name': 'positive_growth_mass_mean', 'disp_name': 'positive growth mass (mean)'}]
                                                     }})

    animal_exploration_gui = ad.gui.ExplorationGUI(explorer=animal_explorer, gui_config=gui_config)
    animal_exploration_gui.run()


if __name__ == '__main__':
    animal_explorer = run_animal_exploration()
    view_exploration_results(animal_explorer)