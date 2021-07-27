from asyncio.tasks import create_task
from flask import (Flask, g, redirect, render_template, request, session, url_for)
import os
import asyncio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def main():
    t1 = create_task(index())
    t2 = create_task(profil())

    await asyncio.wait([t1,t2])
    return redirect(url_for('index'))

@app.route('/index', methods=['GET', 'POST'])
async def index():
    return render_template('index.html')

@app.route('/profil', methods=['GET', 'POST'])
async def profil():
    return render_template('profil.html')

if __name__ == '__main__':
    app.run(debug=True)
    asyncio.run(main())