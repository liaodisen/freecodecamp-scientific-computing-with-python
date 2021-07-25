# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)




# Run unit tests automatically
main(module='test_module', exit=False)