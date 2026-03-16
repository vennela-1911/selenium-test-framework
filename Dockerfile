FROM python:3.10

WORKDIR /app

COPY . .

RUN mkdir -p logs reports/allure-results

RUN chmod -R 777 logs

RUN pip install pytest selenium allure-pytest

CMD ["pytest", "-v", "--alluredir=reports/allure-results"]