import numpy as np
from typing import List, Tuple, Dict

def marcha_aleatoria(n_pasos:int,a:float=1.0)->float:
    pasos=np.random.choice([-a,a],size=n_pasos);return float(np.sum(pasos))

def multiples_marchas(n_pasos:int,n_sims:int)->np.ndarray:
    return np.array([marcha_aleatoria(n_pasos) for _ in range(n_sims)],dtype=float)

def parametros_gaussianos(n_pasos:int)->Tuple[float,float]:
    mu=0.0;sigma=float(np.sqrt(n_pasos));return mu,sigma

def distribucion_gaussiana(x:np.ndarray,mu:float,sigma:float)->np.ndarray:
    return (1.0/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mu)/sigma)**2)

def ejecutar_simulacion(n_pasos:int,n_sims:int)->Dict[str,object]:
    pos_final=multiples_marchas(n_pasos,n_sims)
    media=float(np.mean(pos_final));desv=float(np.std(pos_final))
    mu,sigma=parametros_gaussianos(n_pasos)
    x=np.linspace(float(np.min(pos_final)),float(np.max(pos_final)),1000)
    gauss=distribucion_gaussiana(x,mu,sigma)
    hist,edges=np.histogram(pos_final,bins='auto',density=True)
    centros=(edges[:-1]+edges[1:])/2
    x2=float(np.mean(pos_final**2))
    return {'pos_final':pos_final,'media':media,'desv':desv,'mu':mu,'sigma':sigma,'hist':hist,'centros':centros,'x':x,'gauss':gauss,'n_pasos':n_pasos,'n_sims':n_sims,'x2':x2}

def ejecutar_multiples_n(valores_n:List[int],n_sims:int)->Dict[int,Dict[str,object]]:
    return {n:ejecutar_simulacion(n,n_sims) for n in valores_n}

def constante_difusion(resultados_por_n:Dict[int,Dict[str,object]],delta_t:float=1.0)->Tuple[float,list,list,np.ndarray]:
    n_vals=sorted(resultados_por_n.keys())
    x2_vals=[float(resultados_por_n[n]['x2']) for n in n_vals]
    coeffs=np.polyfit(np.array(n_vals,float),np.array(x2_vals,float),1)
    pendiente=float(coeffs[0]);D=pendiente/(2.0*delta_t)
    return D,n_vals,x2_vals,coeffs

