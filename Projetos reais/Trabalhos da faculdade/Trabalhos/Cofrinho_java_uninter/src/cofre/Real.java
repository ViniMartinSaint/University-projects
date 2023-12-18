package cofre;

public class Real extends Moeda {
	
	public Real(double valor) {
		this.valor = valor;
	}

	
	public void info() {
		System.out.println("Real - " + valor);
		
	}

	
	public double converter() {
		return this.valor * 1;
	}
	
	public boolean equals(Object objeto) {
		if(this.getClass() != objeto.getClass()) {
			return false;
		}
		
		Real objetoReal = (Real) objeto;
		
		if(this.valor != objetoReal.valor) {
			return false;
		}
		return true;
	}

}
