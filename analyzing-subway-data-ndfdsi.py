#!/usr/bin/env python
# coding: utf-8

# # Subway Data Analysis
# 
# ## Introdução
# 
# O sistema de ônibus e trens de Nova Iorque - o Metro Transit Authority - [fornece seus dados para download](http://web.mta.info/developers/developer-data-terms.html#data) através de  arquivos CSV. Dentre as informações disponíveis estão os **registros semanais de dados das catracas do metrô**. 
# 
# 
# Estes registros contém contagens cumulativas das entradas e saídas, normalmente agrupadas em períodos de 4 horas, com dados adicionais que permitem identificar a estação e catraca específica correspondente a cada linha do arquivo. Neste projeto iremos utilizar um desses registros, mas não precisa baixar nada agora! O primeiro exercício será escrever um código Python para fazer isso por você :-)
# 
# 
# 

# # Sobre este projeto
# 
# Neste projeto você irá aplicar todos os conhecimentos adquiridos neste primeiro mês de curso, com tarefas básicas de aquisição e limpeza de dados. No processo iremos descobrir informações essenciais sobre os dados, utilizando o que foi aprendido no curso de estatística. 
# 
# O objetivo deste projeto é explorar a relação entre os dados das catracas do metrô de Nova Iorque e o clima no dia da coleta. Para isso, além dos dados do metrô, precisaremos dos dados de clima da cidade de Nova Iorque. 
# 
# Os principais pontos que serão verificados neste trabalho:
# 
# - Coleta de dados da internet
# - Utilização de estatística para análise de dados
# - Manipulação de dados e criação de gráficos simples com o `Pandas`
# 
# *Como conseguir ajuda*: Sugerimos que busque apoio nos canais abaixo, na seguinte ordem de prioridade:
# 
# | Tipo de dúvida\Canais         	| Google 	| Fórum 	| Slack 	| Email 	|
# |-------------------------------	|--------	|-------	|-------	|-------	|
# | Programação Python e Pandas    	| 1      	| 2     	| 3     	|       	|
# | Requisitos do projeto         	|        	| 1     	| 2     	| 3     	|
# | Partes específicas do Projeto 	|        	| 1     	| 2     	| 3     	|
# 
# Os endereços dos canais são:
# 
# - Fórum: https://discussions.udacity.com/c/ndfdsi-project
# - Slack: [udacity-br.slack.com](https://udacity-br.slack.com/messages/C5MT6E3E1)
# - Email: data-suporte@udacity.com
# 
# **Espera-se que o estudante entregue este relatório com:**
# 
# - Todos os exercícios feitos, com atenção especial para os trechos de código a completar (sinalizados com `# your code here`), pois eles são essenciais para que o código rode corretamente
# - O arquivo ipynb exportado como HTML
# 
# Para entregar este projeto envie este `.ipynb` preenchido e o HTML, zipados, na página correspondente da sala de aula.

# # Sobre o dataset
# 
# Descrição das colunas
# <pre>
# C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS
#   
# C/A      = Agrupamento de catracas de que a catraca faz parte (_Control Area_)
# UNIT     = Cabine de controle associada à estação onde a catraca se encontra (_Remote Unit for a station_)
# SCP      = Endereço específico da catraca (_Subunit Channel Position_)
# STATION  = Nome da estação onde a catraca se encontra
# LINENAME = Código representando todas linhas que passam na estação*
# DIVISION = Código representando a concessionária original da linha, antes da prefeitura assumir a gestão   
# DATE     = Representa a data (no formato MM-DD-YY) do evento de auditoria agendado
# TIME     = Representa o horário (hh:mm:ss) do evento de auditoria agendado
# DESc     = Descreve o tipo de evento de auditoria registrado:
#            1. "REGULAR" representando um evento de auditoria padrão, em que a contagem é feita a cada 4 horas
#            2. "RECOVR AUD" significa que o valor específico estava perdido, mas foi recuperado posteriormente 
#            3. Diversos códigos sinalizam situações em que auditorias são mais frequentes devido a atividades de
#               planejamento ou solução de problemas. 
# ENTRIES  = A contagem cumulativa de entradas associadas à catraca desde o último registro
# EXITS    = A contagem cumulativa de saídas associadas à catraca desde o último registro
# 
# *  Normalmente as linhas são representadas por um caractere. LINENAME 456NQR significa que os trens 4, 5, 6, N, Q e R passam pela estação.
# </pre>

# # Lembretes
# 
# Antes de começarmos, alguns lembretes devem ter em mente ao usar os notebooks iPython:
# 
# - Lembre-se de que você pode ver do lado esquerdo de uma célula de código quando foi executado pela última vez se houver um número dentro das chaves.
# - Quando você inicia uma nova sessão do notebook, certifique-se de executar todas as células até o ponto em que você deixou a última vez. Mesmo que a saída ainda seja visível a partir de quando você executou as células em sua sessão anterior, o kernel começa em um estado novo, então você precisará recarregar os dados, etc. em uma nova sessão.
# - O ponto anterior é útil para ter em mente se suas respostas não correspondem ao que é esperado nos questionários da aula. Tente recarregar os dados e execute todas as etapas de processamento um a um para garantir que você esteja trabalhando com as mesmas variáveis e dados que estão em cada fase do questionário.

# ## Seção 1 - Coleta de Dados
# 
# ### *Exercicio 1.1*
# 
# Mãos a obra!! Agora é sua vez de coletar os dados. Escreva abaixo um código python que acesse o link http://web.mta.info/developers/turnstile.html e baixe os arquivos do mês de junho de 2017. O arquivo deverá ser salvo com o nome turnstile_170610.txt onde 10/06/17 é a data do arquivo.
# 
# <blockquote>
#     <p>Caso o site esteja fora do ar, use essa url:</p>
#     <p>https://s3.amazonaws.com/video.udacity-data.com/topher/2018/November/5bf32290_turnstile/turnstile.html</p>
# </blockquote>
# 
# Abaixo seguem alguns comandos que poderão te ajudar:
# 
# Utilize a biblioteca **urllib** para abrir e resgatar uma página da web. Utilize o comando abaixo onde **url** será o caminho da página da web onde se encontra o arquivo:
# 
# ```python
# u = urllib.urlopen(url)
# html = u.read()
# ```
# 
# Utilize a biblioteca **BeautifulSoup** para procurar na página pelo link do arquivo que deseja baixar. Utilize o comando abaixo para criar o seu objeto *soup* e procurar por todas as tags 'a'no documento:
#  
#  
# ```python
# soup = BeautifulSoup(html, "html.parser")
# links = soup.find_all('a')
# ```
# 
# Uma dica para baixar apenas os arquivos do mês de junho é verificar a data no nome do arquivo. Por exemplo, para baixar o arquivo do dia 17/06/2017 verifique se o link termina com *"turnstile_170610.txt"*. Se não fizer isso você baixará todos os arquivos da página. Para fazer isso utilize o comando conforme abaixo:
# 
# ```python
# if '1706' in link.get('href'):
# ```
# 
# E a dica final é utilizar o comando abaixo para fazer o download do arquivo txt:
# 
# ```python
# urllib.urlretrieve(link_do_arquivo, filename)
# ```
# 
# Lembre-se, primeiro, carregue todos os pacotes e funções que você estará usando em sua análise.

# In[1]:


import urllib
from bs4 import BeautifulSoup

#your code here
import sys
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#Caminho padrão

# path = "http://web.mta.info/developers/" Apresentando erro
path = "https://s3.amazonaws.com/video.udacity-data.com/topher/2018/November/5bf32290_turnstile/"

# URl principal
#url = "http://web.mta.info/developers/turnstile.html" Apresentando erro
url = "https://s3.amazonaws.com/video.udacity-data.com/topher/2018/November/5bf32290_turnstile/turnstile.html"
    
u = urllib.request.urlopen(url)
html = u.read()

# Parser do conteúdo
soup = BeautifulSoup(html, "html.parser")
container = soup.find('div', { 'class': 'container'})
links = container.find_all('a')

for link in links:
    link_str = str(link) 
    if '1706' in link_str and 'udacity' in link_str:
        other_url = link.get('href')
 #       filename = other_url.split("/")[-1]
 #       new_path = f"{path}{other_url}"
        print("other_url:", other_url)
 #       print("filename :", filename) 
 #       print("new_path :", new_path)
        urllib.request.urlretrieve(other_url)
        
        


# ### *Exercicio 1.2*
# 
# Escreva uma função que pegue a lista de nomes dos arquivos que você baixou no exercicio 1.1 e consolide-os em um único arquivo. Deve existir apenas uma linha de cabeçalho no arquivo de saida. 
# 
# Por exemplo, se o arquivo_1 tiver:
# linha 1...
# linha 2...
# 
# e o outro arquivo, arquivo_2 tiver:
# linha 3...
# linha 4...
# linha 5...
# 
# Devemos combinar o arquivo_1 com arquivo_2 em um arquivo mestre conforme abaixo:
# 
# 'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
# linha 1...
# linha 2...
# linha 3...
# linha 4...
# linha 5...
# 
# **OBS:** Note que algumas colunas foram descartadas!

# In[3]:


def create_master_turnstile_file(filenames, output_file):
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')        
        for filename in filenames:
            # your code here            
            #master_file.write(filename + '\n') #- Para Teste
            #line_count = 1 #- Para Teste
            with open(filename) as partial_file:
                for line in partial_file:  
                    #Desconsidera a linha com cabeçalho 
                    if line.startswith("C/A"):                         
                        continue
                    #if line_count > 1 and line_count <= 12: # Para teste
                    # Separa linha para gerar linmha apenas com colunas relevantes 
                    fields = line.split(',')                        
                    new_line = fields[0] + ',' + fields[1] + ',' + fields[2] + ',' + fields[6] + ',' +                                fields[7] + ',' + fields[8] + ',' + fields[9] + ',' + fields[10].rstrip() + '\n' 
                    #print(new_line)                    
                    #master_file.write(line)
                    new_line
                    master_file.write(new_line)
                        
                    #line_count += 1 # - Para teste

days = ['03', '10', '17', '24']
filenames = []
for d in days:
    filenames.append(f"turnstile-1706{d}.txt")

create_master_turnstile_file(filenames, "master_turnstile_201706.txt")


# In[ ]:





# ### *Exercicio 1.3*
# 
# Neste exercício, escreva um função que leia o master_file criado no exercicio anterior e carregue-o em um pandas dataframe. Esta função deve filtrar para que o dataframe possua apenas linhas onde a coluna "DESCn" possua o valor "Regular".
# 
# Por exemplo, se o data frame do pandas estiver conforme abaixo:
#     
#     ,C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn
#     0,A002,R051,02-00-00,05-01-11,00:00:00,REGULAR,3144312,1088151
#     1,A002,R051,02-00-00,05-01-11,04:00:00,DOOR,3144335,1088159
#     2,A002,R051,02-00-00,05-01-11,08:00:00,REGULAR,3144353,1088177
#     3,A002,R051,02-00-00,05-01-11,12:00:00,DOOR,3144424,1088231
# 
# O dataframe deverá ficar conforme abaixo depois de filtrar apenas as linhas onde a coluna DESCn possua o valor REGULAR:
# 
#     0,A002,R051,02-00-00,05-01-11,00:00:00,REGULAR,3144312,1088151
#     2,A002,R051,02-00-00,05-01-11,08:00:00,REGULAR,3144353,1088177
# 

# In[4]:


#import pandas as pd

def filter_by_regular(filename):
    
    turnstile_data = pd.read_csv(filename)
    # more of your code here
    turnstile_data = turnstile_data[turnstile_data.DESCn=='REGULAR']
    return turnstile_data

df_turnstile_reg = filter_by_regular('master_turnstile_201706.txt')


# ### *Exercicio 1.4*
# 
# 
# Os dados do metrô de NY possui dados cumulativos de entradas e saidas por linha. Assuma que você possui um dataframe chamado df que contém apenas linhas para uma catraca em particular (unico SCP, C/A, e UNIT). A função abaixo deve alterar essas entradas cumulativas para a contagem de entradas desde a última leitura (entradas desde a última linha do dataframe).
# 
# Mais especificamente, você deverá fazer duas coisas:
# 
# 1. Criar uma nova coluna chamada ENTRIESn_hourly
# 
# 2. Inserir nessa coluna a diferença entre ENTRIESn da linha atual e a da linha anterior. Se a linha possuir alguma NAN, preencha/substitua por 1.
# 
# Dica: as funções do pandas shift() e fillna() pode ser úteis nesse exercicio.
# 
# Abaixo tem um exemplo de como seu dataframe deve ficar ao final desse exercicio:
# 
#            C/A  UNIT       SCP     DATEn     TIMEn    DESCn  ENTRIESn    EXITSn  ENTRIESn_hourly
#     0     A002  R051  02-00-00  05-01-11  00:00:00  REGULAR   3144312   1088151                1
#     1     A002  R051  02-00-00  05-01-11  04:00:00  REGULAR   3144335   1088159               23
#     2     A002  R051  02-00-00  05-01-11  08:00:00  REGULAR   3144353   1088177               18
#     3     A002  R051  02-00-00  05-01-11  12:00:00  REGULAR   3144424   1088231               71
#     4     A002  R051  02-00-00  05-01-11  16:00:00  REGULAR   3144594   1088275              170
#     5     A002  R051  02-00-00  05-01-11  20:00:00  REGULAR   3144808   1088317              214
#     6     A002  R051  02-00-00  05-02-11  00:00:00  REGULAR   3144895   1088328               87
#     7     A002  R051  02-00-00  05-02-11  04:00:00  REGULAR   3144905   1088331               10
#     8     A002  R051  02-00-00  05-02-11  08:00:00  REGULAR   3144941   1088420               36
#     9     A002  R051  02-00-00  05-02-11  12:00:00  REGULAR   3145094   1088753              153
#     10    A002  R051  02-00-00  05-02-11  16:00:00  REGULAR   3145337   1088823              243

# In[5]:


df_turnstile_reg.info()


# In[6]:


df_turnstile_reg.head(10)


# In[7]:


#import pandas

def get_hourly_entries(df):    
    
    #your code here    
    diff_ENTRIESn = pd.to_numeric(df['ENTRIESn']) - pd.to_numeric(df['ENTRIESn'].shift(1))
    #print(diff_ENTRIESn)
    df['ENTRIESn_hourly'] = diff_ENTRIESn.fillna(1).astype(int) 
    
    return df

df_h_entries = get_hourly_entries(df_turnstile_reg)


# In[8]:


print(df_h_entries)


# ### *Exercicio 1.5*
# 
# Faça o mesmo do exercicio anterior mas agora considerando as saidas, coluna EXITSn.
# Para isso crie uma coluna chamada de EXITSn_hourly e insira a diferença entre a coluna EXITSn da linha atual versus a linha anterior. Se tiver algum NaN, preencha/substitua por 0.
# 
# 

# In[ ]:





# In[9]:


#import pandas

def get_hourly_exits(df):
    
    #your code here
    diff_EXITSn = pd.to_numeric(df['EXITSn']) - pd.to_numeric(df['EXITSn'].shift(1))
    #print(diff_EXITSn)
    df['EXITSn_hourly'] = diff_EXITSn.fillna(0).astype(int) 
    
    return df

df_h_exits = get_hourly_exits(df_h_entries)


# In[10]:


print(df_h_exits)


# In[11]:


df_h_exits.info()


# ### *Exercicio 1.6*
# 
# Dado uma variável de entrada que representa o tempo no formato de:
#      "00:00:00" (hora: minutos: segundos)
#     
# Escreva uma função para extrair a parte da hora do tempo variável de entrada
# E devolva-o como um número inteiro. Por exemplo:
#          
#          1) se a hora for 00, seu código deve retornar 0
#          2) se a hora for 01, seu código deve retornar 1
#          3) se a hora for 21, seu código deve retornar 21
#         
# Por favor, devolva a hora como um número inteiro.
# 

# In[12]:


def time_to_hour(time):    
    hour = int(time.split(':')[0])
    return hour

df_h_exits['HOUR'] = df_h_exits['TIMEn'].map(lambda x: time_to_hour(str(x)))


# In[13]:


df_h_exits.info()


# ## Exercicio 2 - Análise dos dados
# 
# ### *Exercicio 2.1*
# 
# Para verificar a relação entre o movimento do metrô e o clima, precisaremos complementar os dados do arquivo já baixado com os dados do clima.
# Nós complementamos para você este arquivo com os dados de clima de Nova Iorque  e disponibilizamos na área de materiais do projeto. Você pode acessa-lo pelo link: https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
# 
# Agora que temos nossos dados em um arquivo csv, escreva um código python que leia este arquivo e salve-o em um data frame do pandas. 
# 
# Dica: 
# 
# Utilize o comando abaixo para ler o arquivo:
# 
# ```python
# pd.read_csv('output_list.txt', sep=",")
# ```
# 
# 

# In[14]:


#import pandas as pd

filename = "turnstile_data_master_with_weather.csv"

#your code here
df_weather = pd.read_csv(filename, sep=",")


# ### *Exercicio 2.2*
# 
# Agora crie uma função que calcule a quantidade de dias chuvosos, para isso retorne a contagem do numero de dias onde a coluna *"rain"* é igual a 1.
# 
# Dica: Você também pode achar que a interpretação de números como números inteiros ou float pode não
#      funcionar inicialmente. Para contornar esta questão, pode ser útil converter
#      esses números para números inteiros. Isso pode ser feito escrevendo cast (coluna como inteiro).
#      Então, por exemplo, se queríamos lançar a coluna maxtempi como um número inteiro, nós devemos
#      escrever algo como cast (maxtempi as integer) = 76, em oposição a simplesmente
#      onde maxtempi = 76.

# In[15]:



def num_rainy_days(df):
    
    #your code here
    df['rain'] = pd.to_numeric(df['rain'])
    num_days = len(df[df.rain == 1].groupby('DATEn'))
    
    return num_days

num_days_rainy = num_rainy_days(df_weather)


# In[16]:


print(num_days_rainy) 


# ### *Exercicio 2.3*
# 
# Calcule se estava nebuloso ou não (0 ou 1) e a temperatura máxima para fog (isto é, a temperatura máxima 
#      para dias nebulosos).

# In[17]:


def max_temp_aggregate_by_fog(df):
    
    #Converte fog para numero inteiro 
    df['fog'] = pd.to_numeric(df['fog'], errors='coerce').fillna(0).astype(np.int64)    
    
    #df.groupby(['fog'])['maxtempi'].count()    
    #print(df.groupby(['fog'])['maxtempi'].count())
    
    max_tmp = df.groupby(['fog'])['maxtempi'].max()
    
    return max_tmp
    
max_temp_aggregate_by_fog(df_weather)


# ### *Exercicio 2.4
# 
# Calcule agora a média de 'meantempi' nos dias que são sábado ou domingo (finais de semana):

# In[18]:


def avg_weekend_temperature(filename):
    
    df_avg = pd.read_csv(filename, sep=',')
    df_avg['weekday'] = pd.to_datetime(df_avg['DATEn']).dt.dayofweek
    filtered_data = df_avg['meantempi'].astype(float)[df_avg['weekday'] >= 5]
    
    mean_temp_weekends = ("%.2f" % filtered_data.mean())
    
    return mean_temp_weekends

avg_weekend_temperature('turnstile_data_master_with_weather.csv')


# ### *Exercicio 2.5
# 
# Calcule a média da temperatura mínima 'mintempi' nos dias chuvosos onde da temperatura mínima foi maior que do 55 graus:

# In[19]:


def avg_min_temperature(filename):
    df = pd.read_csv(filename, dtype=object)
    filtered_data = df['mintempi'].astype(float)[df['rain'] == '1.0'][df['mintempi'].astype(float) > 55]
    avg_mintemp_on_rainy_days = filtered_data.mean()
    
    avg_min_temp_rainy = ("%.2f" % avg_mintemp_on_rainy_days)
    
    return avg_min_temp_rainy

avg_min_temperature('turnstile_data_master_with_weather.csv')


# ### *Exercicio 2.6
# 
# Antes de realizar qualquer análise, pode ser útil olhar para os dados que esperamos analisar. Mais especificamente, vamos examinR as entradas por hora em nossos dados do metrô de Nova York para determinar a distribuição dos dados. Estes dados são armazenados na coluna ['ENTRIESn_hourly'].
#     
# Trace dois histogramas nos mesmos eixos para mostrar as entradas quando esta chovendo vs quando não está chovendo. 
# Abaixo está um exemplo sobre como traçar histogramas com pandas e matplotlib:
#      
# ```python
# Turnstile_weather ['column_to_graph']. Hist ()
# ```   
#     

# In[ ]:





# In[20]:


#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
       
    
    plt.figure()
    turnstile_weather[turnstile_weather['rain'] == 0]['ENTRIESn_hourly'].hist(alpha=0.45, label="not rainining") # your code here to plot a historgram for hourly entries when it is raining
    turnstile_weather[turnstile_weather['rain'] == 1]['ENTRIESn_hourly'].hist(alpha=0.45, label="rainining") # your code here to plot a histogram for hourly entries when it is not raining
    
    plt.ylabel('Frequency')
    plt.xlabel("Entries per hour")
    plt.legend()
    return plt

entries_histogram(df_weather)


# ### *Exercicio 2.7
# 
# Os dados que acabou de plotar que tipo de ditribuição? Existe diferença na distribuição entre dias chuvosos e não chuvosos?

# **Resposta**:  
# - O retorno para ambos os casos é uma distribuiçao não-normal( assimetrica positiva ).

# ### *Exercicio 2.8
# 
# Construa uma função que que retorne:
# 
# 1. A média das entradas com chuva
# 2. A média das entradas sem chuva
# 
# 
# 

# In[21]:


import numpy as np

import pandas

def means(turnstile_weather):
    
    p = None
    
    ### YOUR CODE HERE ###
    #Converte fog para numero inteiro 
    turnstile_weather['rain'] = pd.to_numeric(turnstile_weather['rain'], errors='coerce').fillna(0).astype(np.int64)    
    
    mean_rain =  turnstile_weather.groupby(['rain'])['ENTRIESn_hourly'].mean()
    with_rain_mean = ("%.2f" % mean_rain[1])
    without_rain_mean =("%.2f" % mean_rain[0])
    
    #return mean_rain
    
    return with_rain_mean, without_rain_mean, p # leave this line for the grader

means(df_weather)


# Responda as perguntas abaixo de acordo com a saida das suas funções:
# 
# 1. Qual a média das entradas com chuva?
# 2. Qual a média das entradas sem chuva?
# 

# **Resposta**: 
# - A média das entradas com chuva é 1105.45. 
# - A média das entradas sem chuva é 1090.28.

# ## Exercicio 3 - Map Reduce
# 
# ### *Exercicio 3.1*
# 
# A entrada para esse exercício e o mesmo arquivo da seção anterior (Exercicio 2). Você pode baixar o arquivo neste link:
# 
#  https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
# 
# Varmos criar um mapeador agora. Para cada linha de entrada, a saída do mapeador deve IMPRIMIR (não retornar) a UNIT como uma chave e o número de ENTRIESn_hourly como o valor. Separe a chave e o valor por uma guia. Por exemplo: 'R002 \ t105105.0'
# 
# Exporte seu mapeador em um arquivo chamado mapper_result.txt e envie esse arquivo juntamente com a sua submissão. O código para exportar seu mapeador já está escrito no código abaixo.
# 
# 
# 

# In[22]:


import sys

def mapper():
    

    for line in sys.stdin:
        # your code here
        
        data = line.strip().split(",")
        
        if data[1] != 'UNIT' and len(data) == 22:
            unit = data[1]
            hour_entries = data[6]
        
            print(f"{unit}\t{hour_entries}")
            
sys.stdin = open('turnstile_data_master_with_weather.csv')
sys.stdout = open('mapper_result.txt', 'w')

mapper()


# ### *Exercicio 3.2*
# 
# Agora crie o redutor. Dado o resultado do mapeador do exercicio anterior, o redutor deve imprimir(Não retornar) uma linha por UNIT, juntamente com o número total de ENTRIESn_hourly.Ao longo de maio (que é a duração dos nossos dados), separados por uma guia. Um exemplo de linha de saída do redutor pode ser assim: 'R001 \ t500625.0'
# 
# Você pode assumir que a entrada para o redutor está ordenada de tal forma que todas as linhas correspondentes a uma unidade particular são agrupados. No entanto a saida do redutor terá repetição pois existem lojas que aparecem em locais diferentes dos arquivos.
# 
# Exporte seu redutor em um arquivo chamado reducer_result.txt e envie esse arquivo juntamente com a sua submissão.

# In[23]:


def reducer():
    entriesTotal = 0
    oldKey = None

    for line in sys.stdin:
        # your code here
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            continue
        
        thisKey, thisEntry = data_mapped
        
        try:
            thisEntry_to_f = float(thisEntry)
            if oldKey and oldKey != thisKey:
                print(f"{oldKey}\t{entriesTotal}")
                oldKey = thisKey
                entriesTotal = 0
            
            oldKey = thisKey
            entriesTotal += thisEntry_to_f
        except ValueError:
            pass
            
sys.stdin = open('mapper_result.txt')
sys.stdout = open('reducer_result.txt', 'w')
        
reducer()


# **Referências**:
# 
#     Udacity - 4. Big Data e Map Reduce (videos and texts) https://classroom.udacity.com/nanodegrees/nd025-br
#     Livro   - Bengfort/Kim, Benjamin/Jenny. Analítica de Dados com Hadoop. Primeira Edição. São Paulo, Novatec, 2016.
# 

# In[ ]:




