#!/bin/bash

echo "Activate autodisc conda environment ..."
source ~/anaconda3/bin/activate autodisc

echo "Start calc Statistics ..."
python -c "import exputils
exputils.start_experiments(directory='./experiments/',
				 start_scripts='run_calc_statistics_over_repetitions.sh',
				 is_parallel=False,
                 is_chdir=True,
				 verbose=True,
				 post_start_wait_time=0.5)"

echo "Finished"
$SHELL

