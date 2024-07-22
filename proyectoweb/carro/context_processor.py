def importe_total_carro(request): #declaramos una variable global
    total=0
    if request.user.is_authenticated: 
     for key,value in request.session["carro"].items():
         total=total+float(value["precio"])
    else:
        total="Debes hacer login"
    return {"importe_total_carro":total}


    #debemos registrar esta variable global dentro de settings en la opcion
    # de templates en la parte 'context_processors'
