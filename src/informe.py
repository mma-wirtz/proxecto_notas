"""Xeración do informe.

FASE 2 · Neste ficheiro traballan AS DÚAS PERSOAS.
"alumnado" é a lista que devolve ler_notas():
[{"nome": "Antía", "nota": 7.5}, {"nome": "Brais", "nota": 4.0}, ...]
"""

from src.estatisticas import media, nota_maxima, nota_minima
from src.clasificacion import contar_aprobados, cualificacion


def seccion_resumo(alumnado):
    """USUARIO 1. Devolve un texto (str) con este formato exacto:

    Alumnado: 6
    Media: 5.92
    Nota máxima: 9.0
    Nota mínima: 3.5
    Aprobados: 4

    Pistas: primeiro crea a lista só coas notas.
    A media leva dous decimais: f"Media: {valor:.2f}"
    Une as liñas con "\\n".join(lista_de_linas)
    """
    notas = [alumno["nota"] for alumno in alumnado]

    lineas = [
        f"Alumnado: {len(alumnado)}",
        f"Media: {media(notas):.2f}",
        f"Nota máxima: {nota_maxima(notas)}",
        f"Nota mínima: {nota_minima(notas)}",
        f"Aprobados: {contar_aprobados(notas)}",
    ]

    return "\n".join(lineas)
    


def seccion_listado(alumnado):
    """USUARIO 2. Devolve un texto (str) cunha liña por alumno/a:

    Antía: 7.5 (Notable)
    Brais: 4.0 (Suspenso)
    ...

    Pistas: percorre a lista cun for e usa cualificacion().
    Une as liñas con "\\n".join(lista_de_linas)
    """
    liñas = []
    for alumno in alumnado:
        nome = alumno["nome"]
        nota = alumno["nota"]
        cualif = cualificacion(nota)
        liñas.append(f"{nome}: {nota} ({cualif})")
    return "\\n".join(liñas)
    


def informe_completo(alumnado):
    """Xunta todas as seccións do informe."""
    partes = ["=== INFORME DE NOTAS ==="]
    # FASE 2: cada persoa engade AQUÍ a chamada á súa sección, por exemplo:
    # partes.append(seccion_xxx(alumnado))
    partes.append(seccion_resumo(alumnado))
    partes.append(seccion_listado(alumnado))
    
    return "\n\n".join(partes)
