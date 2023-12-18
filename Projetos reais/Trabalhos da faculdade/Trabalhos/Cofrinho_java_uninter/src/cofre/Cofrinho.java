package cofre;

import java.util.ArrayList;

public class Cofrinho {
	
	private ArrayList<Moeda> listaMoedas;
	
	public Cofrinho() {
		this.listaMoedas = new ArrayList<>();
	}
	
	public void adicionar(Moeda moeda) {
		this.listaMoedas.add(moeda);
	}
	
	public boolean remover(Moeda moeda) {
		return this.listaMoedas.remove(moeda);
	}

	
	public void listarMoedas() {
		
		if(this.listaMoedas.isEmpty()) {
			System.out.println("Não temno cofrinho!");
			return;
		}
		
		for(Moeda moeda : this.listaMoedas) {
			moeda.info();
		}
	}
	public double calcularTotalEmReais() {
		if (this.listaMoedas.isEmpty()) {
		return 0;	
		}
		
		double somaMoedas = 0;
		
		for(Moeda moeda : this.listaMoedas) {
			somaMoedas = somaMoedas + moeda.converter();
		}
		
		return somaMoedas;
	}
}