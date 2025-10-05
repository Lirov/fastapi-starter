# FastAPI Starter (Routes / Controllers / Services / JWT)

### SETUP
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env .env             # edit values
```

### RUN
```bash
uvicorn app.main:app --reload
```

## TEST
##### REGISTER
```bash
curl -X POST http://127.0.0.1:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","password":"secret123"}'
```

##### LOGIN
```bash
curl -X POST http://127.0.0.1:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","password":"secret123"}'
```

##### ME
```bash
curl http://127.0.0.1:8000/auth/me \
  -H "Authorization: Bearer <ACCESS_TOKEN>"

```
##### HEALTH
```bash
curl http://127.0.0.1:8000/health/live
```

