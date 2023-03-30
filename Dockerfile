FROM python:3.9
WORKDIR /honey-food
COPY ./requirements.txt /honey-food/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /honey-food/requirements.txt
COPY ./app /honey-food/app
COPY ./.env /honey-food/.env

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
