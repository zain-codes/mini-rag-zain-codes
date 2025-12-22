### run app conda environment
```bash
conda activate mini-rag-app-zain-codes
```
### (Optional) Setup you command line interface for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:w\n\[\033[00m\]\$"
```

## Run the FastAPI server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN collection
 Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json]