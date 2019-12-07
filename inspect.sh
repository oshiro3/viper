black --skip-string-normalization viper/main.py
bandit -r viper
flake8 ./viper --count --select=E9,F7,F82 --show-source --statistics
flake8 ./viper --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics