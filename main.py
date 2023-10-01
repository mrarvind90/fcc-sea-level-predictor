# This entrypoint file to be used in development. Start by reading README.md
from src import sea_level_predictor
from unittest import main

# Test your function by calling it here
sea_level_predictor.draw_plot()

# Run unit tests automatically
main(module="tests.test_module", exit=False)
