from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, users, files, services, subscriptions, dashboard

app = FastAPI(title="ReOrg.Data API", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(auth.router,          prefix="/api/auth",          tags=["Authentication"])
app.include_router(users.router,         prefix="/api/users",         tags=["Users"])
app.include_router(files.router,         prefix="/api/files",         tags=["File Management"])
app.include_router(services.router,      prefix="/api/services",      tags=["Services"])
app.include_router(subscriptions.router, prefix="/api/subscriptions", tags=["Subscriptions"])
app.include_router(dashboard.router,     prefix="/api/dashboard",     tags=["Dashboard"])

@app.get("/")
def root():
    return {"message": "ReOrg.Data API is running ✅"}
