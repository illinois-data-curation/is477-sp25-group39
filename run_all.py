import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# define the notebooks to run in order
notebooks = [
    "data_acquisition.ipynb",
    "data_cleaning_preprocessing.ipynb",
    "eda_visualizations.ipynb",
    "final_model_tuning.ipynb"
]

def run_notebook(notebook_path, timeout=600):
    print(f"Running {notebook_path}...")
    try:
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)
            ep = ExecutePreprocessor(timeout=timeout, kernel_name='python3')
            ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path) or '.'}})
        print(f"Completed: {notebook_path}")
    except Exception as e:
        print(f"Failed to run {notebook_path}: {e}")

def main():
    print("Starting end-to-end workflow execution...\n")
    for nb in notebooks:
        run_notebook(nb)
    print("\nWorkflow complete.")

if __name__ == "__main__":
    main()
