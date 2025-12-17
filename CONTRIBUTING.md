# Contributing to MVG

Thanks for your interest in contributing! We're excited to have you help make MVG better.

## Getting Started

### 1. Fork & Clone
```bash
git clone https://github.com/yourusername/mvg.git
cd mvg
```

### 2. Setup Development Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install pytest black flake8 mypy
```

### 3. Make Your Changes
```bash
git checkout -b feature/your-feature-name
# Make your changes
git add .
git commit -m "Clear description of what changed"
```

### 4. Test Before Submitting
```bash
# Run existing tests
python test_mvg.py

# Run pytest if you added tests
python -m pytest

# Check code quality
black .
flake8
mypy . --ignore-missing-imports
```

### 5. Submit Pull Request
- Clear title: "Add feature X" or "Fix issue #Y"
- Describe what changed and why
- Link any related issues
- Include test cases if applicable

## Code Style

We use:
- **Black** for formatting: `black .`
- **Flake8** for linting: `flake8`
- **Type hints** where possible
- **Docstrings** for all functions

Example:
```python
def process_request(
    query: str,
    user_id: str = "default"
) -> Dict:
    """Process a user request with full analysis.
    
    Args:
        query: The user's question or request
        user_id: Unique identifier for the user
        
    Returns:
        Dictionary with response, analysis, and user data
    """
    # Implementation
    pass
```

## Areas for Contribution

### High Priority
- [ ] Database integration (PostgreSQL, MongoDB)
- [ ] Additional AI providers (GPT-4, Llama, etc.)
- [ ] Enhanced error handling
- [ ] Performance optimizations
- [ ] Test coverage expansion

### Medium Priority
- [ ] Web UI (React/Vue dashboard)
- [ ] Mobile app wrapper
- [ ] Multi-language support improvements
- [ ] Documentation improvements
- [ ] Example scripts

### Nice to Have
- [ ] Analytics integration
- [ ] A/B testing framework
- [ ] Custom themes
- [ ] Export/import features
- [ ] Browser extension

## Reporting Issues

Use GitHub Issues to report bugs. Include:

1. **Clear title**: "Shortcut-seeking not detected properly"
2. **Description**: What happened, what was expected
3. **Steps to reproduce**:
   ```bash
   python mvg_production.py
   # Input: "Just do it for me"
   # Expected: redirect
   # Got: proceed
   ```
4. **Environment**:
   - Python version: `python --version`
   - OS: Windows/macOS/Linux
   - Installed packages: `pip freeze`

## Feature Requests

Suggest ideas via GitHub Discussions with:
- Clear use case
- Why it matters
- Potential implementation approach
- Any concerns or blockers

## Questions?

- **Development**: Open a Discussion
- **Design**: Comment on relevant issue
- **Philosophy**: Let's chat via email

## Code of Conduct

Be respectful, inclusive, and constructive. We welcome all backgrounds and experience levels.

## Legal

By contributing, you agree:
- Your work is licensed under the same license (MIT)
- You have permission to contribute
- Respect others' intellectual property

---

## Development Tips

### Running the API During Development
```bash
uvicorn mvg_api:app --reload --host 127.0.0.1 --port 8000
```
The `--reload` flag restarts on file changes.

### Adding a New AI Provider
1. Extend `AIEngine` class
2. Implement `analyze_intent()` and `generate_response()`
3. Add to `AIProvider` enum
4. Update config in `AIConfig`
5. Test with `test_mvg.py`

### Adding Database Support
1. Choose database (PostgreSQL recommended)
2. Create `models.py` with SQLAlchemy schemas
3. Extend `MVGProduction` class
4. Override `process_request()` to save data
5. Add migration scripts

### Writing Tests
```python
import pytest
from mvg_production import MVGProduction, AIConfig, AIProvider

def test_shortcut_detection():
    mvg = MVGProduction(AIConfig(provider=AIProvider.MOCK))
    result = mvg.process_request("Just write my code")
    assert result['analysis']['ethical_decision'] == 'redirect'

def test_genuine_learning():
    mvg = MVGProduction(AIConfig(provider=AIProvider.MOCK))
    result = mvg.process_request("I tried X but got stuck at Y")
    assert result['analysis']['ethical_decision'] == 'proceed'
```

## Review Process

1. **Automated Checks**: Tests, linting, type checking
2. **Code Review**: Maintainers review for quality & philosophy alignment
3. **Discussion**: Questions or suggestions
4. **Approval & Merge**: When ready!

---

Thank you for contributing to making AI that serves human growth! 🚀
