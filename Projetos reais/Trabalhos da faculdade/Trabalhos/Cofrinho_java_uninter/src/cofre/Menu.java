package cofre;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Menu {
    private Scanner sc;
    private Cofrinho cofrinho;

    public Menu() {
        sc = new Scanner(System.in);
        cofrinho = new Cofrinho();
    }

    public void exibirMenuPrincipal() {
        System.out.println("Bem vindo ao cofrinho de Vinícius Maritns: ");
        System.out.println("1 - Adicionar moeda");
        System.out.println("2 - Remover moeda");
        System.out.println("3 - Listar moeda");
        System.out.println("4 - Calcular valor total convertido para real");
        System.out.println("0 - Encerrar");

        String opcaoEscolhida = sc.next();

        switch (opcaoEscolhida) {
            case "0":
                System.out.println("Encerrando o programa.");
                break;
            case "1":
                exibirMenuAuxiliarAdicionarMoedas();
                exibirMenuPrincipal();
                break;

            case "2":
                exibirMenuAuxiliarRemoverMoedas();
                exibirMenuPrincipal();
                break;

            case "3":
                cofrinho.listarMoedas();
                exibirMenuPrincipal();
                break;

            case "4":
                double valorTotalConvertido = cofrinho.calcularTotalEmReais();
                String textoConvertidoTotal = String.valueOf(valorTotalConvertido);
                textoConvertidoTotal = textoConvertidoTotal.replace(",", ".");
                System.out.println("O valor total convertido para real: R$  " + textoConvertidoTotal);
                exibirMenuPrincipal();
                break;

            default:
                System.out.println("Opção inválida!");
                exibirMenuPrincipal();
                break;
        }
    }

    private int obterInputNumerico() {
        while (true) {
            try {
                return sc.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor, insira um número.");
                sc.next(); // Limpa o scanner
            }
        }
    }

    private void exibirMenuAuxiliarAdicionarMoedas() {
        System.out.println("Escolha uma moeda:");
        System.out.println("1 - Real \n2 - Dolar \n3 - Euro");

        int moedaEscolhida;
        try {
            moedaEscolhida = obterInputNumerico();
        } catch (InputMismatchException e) {
            System.out.println("Entrada inválida. Por favor, insira um número correspondente à moeda desejada.");
            exibirMenuPrincipal();
            return;
        }

        System.out.println("Digite o valor:");
        String valorTextoMoeda = sc.next();
        valorTextoMoeda = valorTextoMoeda.replace(",", ".");
        double valorMoeda;
        try {
            valorMoeda = Double.valueOf(valorTextoMoeda);
        } catch (NumberFormatException e) {
            System.out.println("Entrada inválida. Por favor, insira um valor numérico válido.");
            exibirMenuPrincipal();
            return;
        }

        if (moedaEscolhida == 1) {
	    	Real moeda = new Real(valorMoeda);
	    	cofrinho.adicionar(moeda);
	    	System.out.println("Moeda de Real adicionada!");
	    }
	    
	    else if(moedaEscolhida ==2) {
	    	Dolar moeda = new Dolar(valorMoeda);
	    	cofrinho.adicionar(moeda);
	    	System.out.println("Moeda de Dolar adicionada!");
	    }
	    
	    else if(moedaEscolhida == 3) {
	    	Euro moeda = new Euro(valorMoeda);
	    	cofrinho.adicionar(moeda);
	    	System.out.println("Moeda de Real adicionada!");
	    }
	    else {
	    	System.out.println("Não existe essa moeda");
	    	exibirMenuPrincipal();
	    }
    }

    private void exibirMenuAuxiliarRemoverMoedas() {
        System.out.println("Escolha uma moeda:");
        System.out.println("1 - Real \n2 - Dolar \n3 - Euro");

        int moedaEscolhida;
        try {
            moedaEscolhida = obterInputNumerico();
        } catch (InputMismatchException e) {
            System.out.println("Entrada inválida. Por favor, insira um número correspondente à moeda desejada.");
            exibirMenuPrincipal();
            return;
        }

        System.out.println("Digite o valor:");
        String valorTextoMoeda = sc.next();
        valorTextoMoeda = valorTextoMoeda.replace(",", ".");
        double valorMoeda;
        try {
            valorMoeda = Double.valueOf(valorTextoMoeda);
        } catch (NumberFormatException e) {
            System.out.println("Entrada inválida. Por favor, insira um valor numérico válido.");
            exibirMenuPrincipal();
            return;
        }

        Moeda moeda = null;
	    
	    if (moedaEscolhida == 1) {
	    	moeda = new Real(valorMoeda);
	    }
	    else if(moedaEscolhida ==2) {
	    	moeda = new Dolar(valorMoeda);
	    }
	    else if(moedaEscolhida == 3) {
	    	moeda = new Euro(valorMoeda);
	    }
	    else {
	    	System.out.println("Não existe essa moeda");
	    	exibirMenuPrincipal();
	    }
	    
	    boolean moedaRemovida = cofrinho.remover(moeda);
	    
	    if(moedaRemovida) {
	    	System.out.println("Moeda Removida!");
	    } else {
	    	System.out.println("Moeda não econtrada");
	    }
	    
   }
}