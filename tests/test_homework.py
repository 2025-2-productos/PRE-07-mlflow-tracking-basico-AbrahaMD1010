import subprocess
import sys


def test_01():
    try:
        for model in ["elasticnet", "knn"]:
            subprocess.run(
                [sys.executable, "-m", "homework", "--model", model],
                check=True,
            )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")
