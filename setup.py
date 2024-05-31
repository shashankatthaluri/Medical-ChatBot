from setuptools import find_packages, setup

setup(
    name="medical_chatbot",
    version="0.0.1",
    author="Shashank atthaluri",
    author_email="shashankatthaluri@gmail.com",
    install_requires=["ctransformers==0.2.5","sentence-transformers==2.2.2", "pinecone-client", "langchain", "flask"],
    packages=find_packages()         
)