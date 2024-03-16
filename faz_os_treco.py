from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from typing import Literal
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
import os

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.



Categoria = Literal["criptomoedas", "agro", "exterior"]

class ArtigoPydantic(BaseModel):
    """Artigo em português resumido"""
    titulo: str = Field(description="Título que resume o ponto do texto")
    categoria: Categoria = Field(description="Categoria que o artigo se enquadra")
    pontos_chave: list[str] = Field(description="Pontos chave do artigo")



def faz_treco_la_de_resumir(artigo):
    key = os.environ.get("OPENAI_API_KEY")
    model = ChatOpenAI(openai_api_key=key)

    parser = JsonOutputParser(pydantic_object=ArtigoPydantic)

    prompt = PromptTemplate(
        template="Responda a seguinte query em portugues:\n{format_instructions}\n{texto}\n",
        input_variables=["texto"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | model | parser
    return chain.invoke({"texto": artigo.texto})

