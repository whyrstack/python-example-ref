```bash
docker compose up -d
python3 main.py
docker exec -it postgres17 psql -U myuser -d mydb -c "\dt"
docker exec -it postgres17 psql -U myuser -d mydb -c "SELECT * FROM users;"
docker compose down -v
```