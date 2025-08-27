from logic import ejecutar_simulacion, ejecutar_multiples_n, constante_difusion
import numpy as np
import matplotlib.pyplot as plt

def graficar_histograma(res:dict):
    fig,ax=plt.subplots(figsize=(10,6))
    conteo,edges=np.histogram(res['pos_final'],bins='fd',density=True)
    ax.bar((edges[:-1]+edges[1:])/2,conteo,width=edges[1]-edges[0],color='orange',alpha=0.6,align='center',label='Simulación')
    ax.fill_between(res['x'],res['gauss'],color='blue',alpha=0.3,label='Gauss teórica')
    ax.set_title(f"Distribución final de posiciones (N={res['n_pasos']}, sims={res['n_sims']})")
    ax.set_xlabel('Posición');ax.set_ylabel('Probabilidad');ax.legend();ax.axvline(0,color='k',linestyle=':')
    plt.tight_layout();plt.show()

def graficar_trayectorias(n_pasos:int,muestras:int=50):
    fig,ax=plt.subplots(figsize=(10,6))
    colores=plt.cm.viridis(np.linspace(0,1,min(muestras,50)))
    for i in range(min(muestras,50)):
        pasos=np.random.choice([-1,1],size=n_pasos);tray=np.cumsum(pasos)
        ax.plot(range(n_pasos),tray,color=colores[i],alpha=0.8)
    ax.set_title(f"Ejemplos de trayectorias aleatorias (N={n_pasos})")
    ax.set_xlabel('Paso');ax.set_ylabel('Posición');ax.axhline(0,color='gray',linestyle='--')
    plt.tight_layout();plt.show()

def graficar_x2_vs_n(resultados_por_n:dict,D:float,coef):
    n=list(resultados_por_n.keys())
    x2=[resultados_por_n[k]['x2'] for k in n]
    fig,ax=plt.subplots(figsize=(10,6))
    sizes=np.linspace(30,100,len(n))
    ax.scatter(n,x2,c=x2,cmap='plasma',s=sizes,edgecolors='k',label='Simulado')
    p=np.poly1d(coef);x=np.linspace(min(n),max(n),200);y=p(x)
    ax.plot(x,y,'b--',linewidth=2,label='Ajuste lineal')
    ax.plot(n,n,'r-.',linewidth=2,label='Teórico N')
    ax.set_title(f"Crecimiento de ⟨x²⟩ con N (D≈{D:.4f})")
    ax.set_xlabel('Número de pasos (N)');ax.set_ylabel('⟨x²⟩ acumulado')
    ax.legend();ax.grid(alpha=0.4)
    plt.tight_layout();plt.show()

def main():
    print('=== Marcha Aleatoria Unidimensional ===')
    print('1. Histograma (Punto 7)')
    print('2. ⟨x²⟩ vs N (Punto 8)')
    op=input('Opción (1/2): ')
    if op=='1':
        n_pasos=int(input('N: '));n_sims=int(input('Simulaciones: '))
        res=ejecutar_simulacion(n_pasos,n_sims)
        graficar_histograma(res)
    elif op=='2':
        n_sims=int(input('Simulaciones por N: '))
        n_min=int(input('N mínimo: '));n_max=int(input('N máximo: '));n_step=int(input('Salto N: '))
        n_vals=list(range(n_min,n_max+1,n_step))
        resultados_por_n=ejecutar_multiples_n(n_vals,n_sims)
        D,n_vals_list,x2_list,coef=constante_difusion(resultados_por_n)
        print('\nN      ⟨x²⟩(sim)   ⟨x²⟩(teo)   |dif|     error%')
        print('-'*48)
        for n in n_vals:
            sim=float(resultados_por_n[n]['x2']);teo=float(n)
            dif=abs(sim-teo);err=0.0 if teo==0 else dif/teo*100.0
            print(f"{n:6d} {sim:11.4f} {teo:11.4f} {dif:8.4f} {err:8.2f}")
        graficar_x2_vs_n(resultados_por_n,D,coef)
    else:
        print('Opción no válida.')

if __name__=='__main__':
    main()
