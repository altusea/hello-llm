import os

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

if __name__ == "__main__":
    # get project's root dir
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    documents = SimpleDirectoryReader(root_dir + "/data").load_data()
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    query_engine = index.as_query_engine()
    response = query_engine.query("Some question about the data should go here")
    print(response)
