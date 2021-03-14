def calculo_bayes(evento, hipotesis, prior, prob_dado_evento, prob_evento):
    prob_hipotesis_dado_evento= (prior*prob_dado_evento)/prob_evento
    print(f'la probabilidad de {hipotesis} dado {evento} es {round(prob_hipotesis_dado_evento*100,3)}%')
    return int(prob_hipotesis_dado_evento)

def sintomas (prob_hipotesis):

    
    prob_sintoma_dado_cancer=1
    prob_sintoma_dado_no_cancer=10/99999
    prob_no_cancer=99999/100000
    prob_cancer= (prob_hipotesis*prob_sintoma_dado_cancer+prob_sintoma_dado_no_cancer*prob_no_cancer)
    calculo_bayes('un síntoma', 'tener cáncer',prob_hipotesis, prob_sintoma_dado_cancer, prob_cancer )

def spam(evento, prob_spam_y_perro):
    ### encontrar probabilidad de que sea spam dado salga la palabra 'perro' en un correo (datos inventados )
    prob_perro_dado_spam= 1/29
    prob_perro_dado_no_spam= 11/71
    prob_no_spam= 71/100
    prob_perro= (prob_spam_y_perro*prob_perro_dado_spam+prob_no_spam*prob_perro_dado_no_spam)
    calculo_bayes('que sea spam', evento, prob_spam_y_perro, prob_perro_dado_spam, prob_perro)

    


if __name__=='__main__':
    prob_cancer_dado_sintoma= sintomas(0.009091)
    prob_spam_dado_perro= (spam('la palabra perro está en el email', 29/100)) 
     
    

