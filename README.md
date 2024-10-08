# NYT_Scraper  
A Python app that collects data from the NYT API and summarizes it using LLMs  
## Project Structure  
```  
├── app/           # Main package  
│   ├── __init__.py           
│   ├── core/               # Core functionality (business logic)  
│   │   ├── __init__.py  
│   │   └── core_module.py  
│   │  
│   ├── services/           # Services (API clients, integrations)  
│   │   ├── __init__.py  
│   │   └── service_module.py  
│   │  
│   ├── models/             # Data models (database models, schemas)  
│   │   ├── __init__.py  
│   │   └── model_module.py  
│   │  
│   ├── utils/              # Utility functions and helpers  
│   │   ├── __init__.py  
│   │   └── utils_module.py  
│   │  
│   ├── config/             # Configuration files  
│   │   ├── __init__.py  
│   │   └── config.py       # Environment config for API keys, URLs, etc. 
│   │   └── logging_config.py   # Logging configuration for the whole program  
│   │  
│   ├── tests/              # Test suite  
│   │   ├── __init__.py  
│   │   └── test_module.py  
│   │  
│   └── main.py             # Entry point  
│  
├── .env                    # Environment variables  
├── .gitignore                
├── requirements.in         # Manually maintained list of primary dependencies: Packages that this project directly needs to run
├── requirements.txt        # Auto-generated list of all dependecies with sub-dependencies (packages that primary dependencies need to run) included
├── requirements-dev.txt    # Optional dev deps not needed in prod, used for testing + formatting             
├── pyproject.toml                
└── README.md               # Long description of package
 ```  
## Dependency Management Workflow  
The `pip-compile` workflow to separate out primary dependencies (direct deps) and sub-dependencies (sub-deps).  
This workflow can be used for syncing virtual environments, dependency version pinning, and automated dependency resolution:  
1. Manually-maintain list of direct dependencies in `requirements.in`.   
2. Handling of sub-dependencies are delegated to `pip-compile`
3. Pin versions of all sub-dependencies and    
4. `$ pip-sync requirements.txt requirements-dev.txt`
	1. Ensure 
## System Design