# Michelin Map — Interactive Global Michelin-star Restaurant Explorer

## What is this

This repository provides a minimal pipeline and interactive web-map of restaurants listed in the Michelin Guide. It loads a public dataset of Michelin-starred restaurants (1, 2, 3 stars), cleans the data, and renders an interactive world map where you can filter by star rating and — if available — by sustainability (green-star) status.

## Data Source

- Dataset from `ngshiheng/michelin-my-maps` (MIT license) — a global collection of Michelin restaurants with coordinates, award type, cuisine, address, etc. :contentReference[oaicite:7]{index=7}  


## How to use

1. Clone the repo  
2. Download the dataset and place the CSV into `data/raw/michelin_my_maps.csv`  
3. (Optional) Inspect / explore with `notebooks/EDA.ipynb`  
4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the web app:

    ```bash
    python src/app.py
    ```

6. Open your browser at `http://127.0.0.1:5000/` to view the interactive map.

## Next steps / extensions

- Add filters by cuisine, country, price category, etc.  
- Add clustering or region-level aggregations (e.g. by country, city)  
- Add historical data (if you gather multiple years) to explore evolution over time  
- Use a database instead of a flat CSV if you want incremental updates or user annotations  
- Deploy to a cloud / hosting platform (Heroku, Render, etc.)  

## License

MIT (for code). Data license as per the original dataset (MIT).
