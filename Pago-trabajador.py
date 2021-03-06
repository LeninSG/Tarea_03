#encoding:UTF-8
#Autor:Lenin Silva Gutiérrez, A01373214 , A01373214,
#Calcula el pago de un trabajador

#calcula el pago que recibe el trabajador y regresa su valor
def calcularPagoNormal(horas, pago_hora):
    pago=horas*pago_hora
    return pago

#calcula el pago extra que recibe el trabajador y regresa su valor
def calcularPagoExtra(horas_extra, pago_hora):
    #el pago extra es 50% más por el mismo tiempo. Por eso, se calcula el pago normal poniendo como tiempo trabajado
    #el de las horas extra y semultiplica por 1.5
    pago_extra=calcularPagoNormal(horas_extra, pago_hora)*1.5 
    return pago_extra

def main():
    horas=int(input("Horas normales trabajadas"))#lee las horas trabajadas
    horas_extra=int(input("Horas extra trabajadas"))#lee las horas extra trabajadas
    pago_hora=float(input("Pago por hora"))#lee el pago por hora
    pago_normal=calcularPagoNormal(horas, pago_hora)
    pago_extra= calcularPagoExtra(horas_extra, pago_hora)
    pago_total=pago_normal+pago_extra
    print ("Horas %s: %d"%("normales",horas))
    print ("Horas %s: %d"%("extra",horas_extra))
    print ("Pago por hora: $%.2f"%(pago_hora))
    print ("Pago semanal %s: $%.2f"%("normal", pago_normal))
    print ("Pago semanal %s: $%.2f"%("extra",pago_extra))
    print ("Pago semanal %s: $%.2f"%("total",pago_total))

main()
