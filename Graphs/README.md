# LangGraph *GRAPH* Examples

This repository contains a collection of interactive Jupyter notebooks illustrating various features and patterns of **LangGraph**, a Python library for building stateful computation graphs. Each notebook builds on the previous one, showcasing progressive levels of complexity—from basic node chaining to conditional branching and multi-step pipelines.

## Prerequisites

* Python 3.8 or higher
* Jupyter Notebook or JupyterLab
* **LangGraph** library (install via PyPI)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/unikill066/GenAI_LangChain.git
   cd Graphs
   ```
2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   .\venv\Scripts\activate     # Windows
   ```
3. Install dependencies:

   ```bash
   pip install langgraph jupyter
   ```

## Running the Notebooks

Launch Jupyter and open any notebook to explore the examples:

```bash
jupyter lab   # or `jupyter notebook`
```

Follow the step-by-step code cells and markdown explanations. You can modify input values or add new nodes to experiment with LangGraph’s API.

## Notebook Summaries

### 1. Basic State Graph (`langgraph_graph_1.ipynb`)

Defines a minimal `StateGraph` with two arithmetic nodes and runs a demo invocation.

### 2. Chained Nodes and Routers (`langgraph_graph_2.ipynb`)

Introduces explicit router nodes and shows how to chain multiple processing steps.

### 3. Sequential Graph Pattern (`langgraph_graph_3_seq_graph.ipynb`)

Refactors the pipeline into a pure sequential flow without manual router nodes.

### 4. Conditional Branching (`langgraph_graph_4_conditional_graph.ipynb`)

Implements `graph.add_conditional_edges` to dynamically choose graph paths at runtime.

### 5. Multi-Step Conditional Pipeline (`langgraph_graph_5.ipynb`)

Combines two decision points and four operation nodes, demonstrating a complete two-stage conditional workflow.

## Contributing

Contributions and feedback are welcome! Feel free to submit issues or pull requests to improve examples, add new patterns, or update documentation.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Citations:
Source: https://www.youtube.com/watch?v=jGg_1h0qzaM