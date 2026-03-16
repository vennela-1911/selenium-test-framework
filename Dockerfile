FROM python:3.10

WORKDIR /app

COPY . .

RUN mkdir -p logs reports/allure-results

RUN pip install pytest selenium

CMD ["pytest", "-v", "--alluredir=reports/allure-results"]