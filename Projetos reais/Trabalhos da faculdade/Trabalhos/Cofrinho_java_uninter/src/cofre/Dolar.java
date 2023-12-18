package cofre;

public class Dolar extends Moeda{
	
	public Dolar(double valor) {
		this.valor = valor;
	}

	@Override
	public void info() {
		System.out.println("Dolar - " + valor);
		
	}

	@Override
	public double converter() {
		return valor * 4.98; // Cotação do dia 30 de out., 03:21 UTC
	}
	
	@Override
	public boolean equals(Object objeto) {
		if(this.getClass() != objeto.getClass()) {
			return false;
		}
		
		Dolar objetoDolar = (Dolar) objeto;
		
		if(this.valor != objetoDolar.valor) {
			return false;
		}
		return true;
	}

}
