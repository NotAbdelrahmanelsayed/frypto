# To-Do List

### 🛠️ Pending Tasks
- [ ] Import the package to ReadTheDocs for automatic documentation generation.  
- [ ] Create a Docker container to simplify contributions and setup.  
- [ ] Refactor to inherit `extract_features` from `allfeatures` in other classes, if applicable.  
- [ ] Set up Continuous Integration (CI) for automated testing and checks.  
- [ ] Optimize performance:
  - Use profiling tools to identify bottlenecks.
  - Implement multiprocessing where possible to enhance computation speed.

---

### ✅ Completed Tasks
- [x] Create a `requirements.txt` file.  
- [x] Write a `README.md` file.  
- [x] Add a `notebooks` directory for quickstart examples.  
- [x] Ensure the main script processes the entire DataFrame and utilizes all available classes.  
- [x] Add a script to rename columns for consistency (e.g., `close/CLOSE` → `Close`).  
- [x] Write unit tests for the `allfeatures` class.  
- [x] Move price change functionality to the main script and pass it to other classes (e.g., `volume_features`, `price_features`).  
- [x] Select an appropriate license using [choosealicense.com](https://choosealicense.com).  
- [x] Add a `MANIFEST.in` file.  
- [x] Write a `setup.py` file for package installation.  
- [x] Include a `pyproject.toml` file.  
- [x] Integrate `numba` for performance improvements.
