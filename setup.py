from setuptools import setup, find_packages

setup(
    name="mvg",
    version="4.0.0",
    description="AI-powered ethical guidance system for human growth",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="The Qayyim & Contributors",
    author_email="contact@example.com",
    url="https://github.com/yourusername/mvg",
    license="MIT",
    packages=find_packages(where="."),
    py_modules=[
        "mvg_production",
        "mvg_ai_enhanced",
        "mvg_system_core",
        "mvg_api",
        "test_mvg"
    ],
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0",
        "anthropic>=0.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="ai education ethics growth guidance learning",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/mvg/issues",
        "Documentation": "https://github.com/yourusername/mvg#readme",
        "Source": "https://github.com/yourusername/mvg",
    },
)
