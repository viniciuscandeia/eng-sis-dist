from flask import Flask, render_template, request
import calendar
from datetime import date

app = Flask(__name__)

@app.route('/')
def calendario():
    # Obter o ano e mês atual
    ano = date.today().year
    mes = date.today().month

    # Verificar se o usuário solicitou um mês/ano diferente
    ano_param = request.args.get('ano')
    mes_param = request.args.get('mes')

    if ano_param and mes_param:
        ano = int(ano_param)
        mes = int(mes_param)
    elif ano_param: # Se só o ano foi alterado, usa o mês atual
        ano = int(ano_param)
        mes = date.today().month


    # Gerar o calendário HTML usando a biblioteca calendar do Python
    cal = calendar.HTMLCalendar(calendar.MONDAY) # Define que a semana começa na segunda-feira
    calendario_html = cal.formatmonth(ano, mes)

    # Formatar o nome do mês e ano para exibir no topo do calendário
    nome_mes = calendar.month_name[mes]
    titulo_calendario = f"{nome_mes} de {ano}"

    # Calcular mês e ano anterior e próximo para os links de navegação
    mes_anterior = mes - 1
    ano_anterior = ano
    if mes_anterior < 1:
        mes_anterior = 12
        ano_anterior -= 1

    mes_proximo = mes + 1
    ano_proximo = ano
    if mes_proximo > 12:
        mes_proximo = 1
        ano_proximo += 1

    return render_template(
        'index.html',
        calendario_html=calendario_html,
        titulo_calendario=titulo_calendario,
        mes_anterior=mes_anterior,
        ano_anterior=ano_anterior,
        mes_proximo=mes_proximo,
        ano_proximo=ano_proximo
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')