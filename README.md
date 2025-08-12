# Bajaj Policy MVP RAG

## API Endpoint Overview

This project exposes a FastAPI endpoint for advanced Retrieval-Augmented Generation (RAG) over insurance, academic, and legal documents.  
**Main endpoint:**  
- `POST /hackrx/run`  
  - Accepts:  
    - `documents`: URL to a document (PDF, PPT, DOCX, XLSX, image, etc.)
    - `questions`: List of questions to answer from the document
  - Returns:  
    - Answers for each question, leveraging embeddings, hybrid retrieval, and NVIDIA LLM.

Other endpoints:
- `GET /health` — Health check
- `GET /cache/stats` — Cache statistics
- `DELETE /cache/clear` — Clear embedding cache

## Workflow

```mermaid
graph TD
    subgraph "Request Pipeline"
        A[User Request: /hackrx/run] --> B{Input Validation};
        B --> C[Get NVIDIA API Key];
        C --> D{Download & Detect File};
        D -- Binary/Archive --> E[Answer from Knowledge];
        D -- Other Formats --> F{Cache Check};
        F -- Cache Hit --> G[Load from Cache];
        F -- Cache Miss --> H[Process File];
        H --> I[Chunk & Embed];
        I --> J[Create FAISS Vectorstore];
        J --> K[Save to Cache];
        K --> G;
        G --> L[Detect Document Type];
        L --> M{Process Questions};
    end

    subgraph "Question Processing Loop"
        M --> N[Preprocess Question];
        N --> O[Classify Question];
        O --> P[Get Retrieval Params];
        P --> Q[Hybrid Retrieval];
        Q --> R[LLM Call];
        R --> S[Clean & Trim Answer];
        S --> T[Add to Context History];
        T --> M;
    end

    subgraph "Response Generation"
        M -- All Questions Processed --> U[Gather Answers];
        U --> V[Save Results to JSON];
        V --> W[Return Final Response];
    end

    style E fill:#f9f,stroke:#333,stroke-width:2px
```

## Frontend MVP

The MVP frontend is built with React (see `frontend/`).  
- Features a dashboard, chat bar, sidebar, and metric cards.
- Uses Tailwind CSS for styling.
- Connects to the API endpoint for document Q&A.
- Designed for rapid prototyping and user feedback.

## Product Screenshot

![Product Screenshot](Screenshot%202025-08-10%20230656.png)

## How to Start

**Backend (API):**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server (with ngrok for public URL)
python api_main_v2.py
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

Access the frontend at [http://localhost:3000](http://localhost:3000) and connect to the API endpoint as configured.

## Tech Stack

- FastAPI, Python, LangChain, HuggingFace Embeddings, FAISS, NVIDIA LLM
- React, Tailwind CSS (frontend)
- Advanced caching, multi-format document loaders, hybrid retrieval

## License

MIT
