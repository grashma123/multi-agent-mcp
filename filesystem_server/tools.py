import os

def list_files(path="."):
    try:
        files = os.listdir(path)
        return {"files": files}
    except Exception as e:
        return {"error": str(e)}

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return {"content": f.read()}
    except Exception as e:
        return {"error": str(e)}