# FAIRWork-Knolwedge-Base-Swagger-Client
This repository functions as an invaluable tool for developers aiming to seamlessly and efficiently integrate and interface with the knowledge base. The code has been generated through the utilization of a Docker image of the Swagger Editor. This method facilitated the automatic generation of Python client-side code by leveraging the Swagger documentation provided by Jonte. This process ensures that communication operates as anticipated and provides type hints for a convenient development experience.
Moreover, this repository presents a structured approach to managing credentials and authentication. Additionally, it includes practical examples that demonstrate how to effectively interact with the knowledge base. These examples have been adapted from Jonte's Jupyter examples. Serving as practical guides, they provide developers with a hands-on experience in effectively utilizing the generated Python client-side code.

## Quick Start
the following steps will get you started with the knowledge base client-side code using [PyCharm](https://www.jetbrains.com/de-de/pycharm/):
1. Clone the repository
2. Install the requirements by running `pip install -r requirements.txt`
3. mark the `src` folder as a source root (in your IDE)
4. mark the `resources` folder as a resource root
5. add the files `knowledge_base_config.yaml` and `knowledge_base_credentials.yaml` to the `resources` folder (NOTE: these files are not included in the repository for security reasons). However, examples for their structure are provided.
6. run `adapted_jotne_example.py` to see an example of how to use the client-side code (NOTE: make sure the working directory of your run configuration is set to the root of the project)

