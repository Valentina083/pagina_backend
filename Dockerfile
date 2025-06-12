FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
# Recolectar estáticos para admin y DRF
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "proyecto_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
