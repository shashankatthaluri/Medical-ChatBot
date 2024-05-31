from setuptools import find_packages, setup

setup(
    name="medical_chatbot",
    version="0.0.1",
    author="Shashank atthaluri",
    author_email="shashankatthaluri@gmail.com",
    packages=find_packages(),
    install_requires=["ctransformers==0.2.5","sentence-transformers==2.2.2", "pinecone-client", "langchain==0.0.255", "flask"]         
)