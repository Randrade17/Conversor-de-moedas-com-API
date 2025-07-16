import requests

def obter_taxa_cambio(origem, destino):
    
    url = f"https://api.exchangerate.host/convert?from={origem}&to={destino}"
    resposta = requests.get(url)
    dados = resposta.json()
    
    if resposta.status_code != 200 or not dados.get("success", True):
        raise Exception("Erro ao obter taxa de câmbio")
    
    return dados["info"]["rate"]

    return dados["info"]["rate"]

def converter_moeda(origem, destino, valor):
    taxa = obter_taxa_cambio(origem, destino)
    convertido = valor * taxa
    return convertido, taxa

def main():
    print("💱 Conversor de Moedas com API (ExchangeRate.host)\n")

    try:
        origem = input("Digite a moeda de origem (ex: USD): ").upper()
        destino = input("Digite a moeda de destino (ex: BRL): ").upper()
        valor_str = input(f"Digite o valor em {origem}: ")
        if not valor_str.replace('.', '', 1).isdigit():
            raise ValueError("Valor numérico inválido.")
        valor = float(valor_str)
        convertido, taxa = converter_moeda(origem, destino, valor)

        print(f"\n🔄 Taxa de câmbio atual: 1 {origem} = {taxa:.4f} {destino}")
        print(f"🪙 {valor:.2f} {origem} = {convertido:.2f} {destino}")
    
    except Exception as e:
        print("❌ Ocorreu um erro:", str(e))

if __name__ == "__main__":
    main()
