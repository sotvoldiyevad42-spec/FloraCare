# FloraCare
I want to create FloraCare, a comprehensive digital platform that serves as a natural plant care guide and flower shop aggregator

FloraCare/
├── main.py              # FastAPI entry point
├── users/
│   ├── routes.py        # /register, /login, /logout
│   ├── models.py        # User, Seller, Buyer
│   └── schemas.py       # Pydantic schemas
├── plants/
│   ├── routes.py        # Gullar CRUD
│   └── models.py
├── shops/
│   ├── routes.py        # Do'konlar + lokatsiya
│   └── models.py
├── ai/
│   └── routes.py        # AI chat endpoint
└── database.py          # PostgreSQL / SQLite
quizzes
---->models.py
---->routs.py