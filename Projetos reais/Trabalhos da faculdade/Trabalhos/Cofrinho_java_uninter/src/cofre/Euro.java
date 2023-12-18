package cofre;

public class Euro extends Moeda {
	
	public Euro(double valor) {
		this.valor = valor;
	}

	
	public void info() {
		System.out.println("Euro - " + valor);
		
	}

	
	public double converter() {
		return this.valor * 5.26; // Cotação do dia 30 de out., 03:49 UTC
				
	}
	
	@Override
	public boolean equals(Object objeto) {
		if(this.getClass() != objeto.getClass()) {
			return false;
		}
		
		Euro objetoEuro = (Euro) objeto;
		
		if(this.valor != objetoEuro.valor) {
			return false;
		}
		return true;
	}
	

}