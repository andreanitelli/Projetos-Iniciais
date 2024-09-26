using System;
using System.Collections.Generic;

public class Program
{
    public class Produto
    {
        public string Descricao { get; set; }
        public string TipoUnidade { get; set; }
        public decimal Valor { get; set; }
        public int Quantidade { get; set; }

        public Produto(string descricao, string tipoUnidade, decimal valor, int quantidade)
        {
            Descricao = descricao;
            TipoUnidade = tipoUnidade;
            Valor = valor;
            Quantidade = quantidade;
        }

        public override string ToString()
        {
            return $"Descrição: {Descricao}, Tipo de Unidade: {TipoUnidade}, Valor: R${Valor}, Quantidade: {Quantidade}";
        }
    }

    private static List<Produto> produtos = new List<Produto>();

    public static void Main()
    {
        int opcao;
        do
        {
            Console.Clear();
            Console.WriteLine("[1] Novo");
            Console.WriteLine("[2] Listar Produtos");
            Console.WriteLine("[3] Remover Produtos");
            Console.WriteLine("[4] Entrada Estoque");
            Console.WriteLine("[5] Saída Estoque");
            Console.WriteLine("[0] Sair");
            Console.Write("Escolha uma opção: ");
            opcao = int.Parse(Console.ReadLine());

            switch (opcao)
            {
                case 1:
                    Novo();
                    break;
                case 2:
                    ListarProdutos();
                    break;
                case 3:
                    RemoverProduto();
                    break;
                case 4:
                    EntradaEstoque();
                    break;
                case 5:
                    SaidaEstoque();
                    break;
                case 0:
                    Console.WriteLine("Saindo...");
                    break;
                default:
                    Console.WriteLine("Opção inválida!");
                    break;
            }

           
        } while (opcao != 0);
    }

    private static void Novo()
    {
        Console.Clear();
        Console.Write("Descrição do Produto: ");
        string descricao = Console.ReadLine();
        Console.Write("Tipo de Unidade: ");
        string tipoUnidade = Console.ReadLine();
        Console.Write("Valor em R$: ");
        decimal valor = decimal.Parse(Console.ReadLine());
        Console.Write("Quantidade: ");
        int quantidade = int.Parse(Console.ReadLine());

        Produto produto = new Produto(descricao, tipoUnidade, valor, quantidade);
        produtos.Add(produto);
        Console.WriteLine("Produto cadastrado com sucesso!");
    }

    private static void ListarProdutos()
    {
        Console.Clear();
        if (produtos.Count == 0)
        {
            Console.WriteLine("Nenhum produto cadastrado.");
            return;
        }

        foreach (Produto produto in produtos)
        {
            Console.WriteLine(produto);
        }
    }

    private static void RemoverProduto()
    {
        Console.Clear();
        Console.Write("Descrição do Produto a ser removido: ");
        string descricao = Console.ReadLine();

        Produto produto = produtos.Find(p => p.Descricao.Equals(descricao, StringComparison.OrdinalIgnoreCase));

        if (produto != null)
        {
            produtos.Remove(produto);
            Console.WriteLine("Produto removido com sucesso!");
        }
        else
        {
            Console.WriteLine("Produto não encontrado.");
        }
    }

    private static void EntradaEstoque()
    {
        Console.Clear();
        Console.Write("Descrição do Produto: ");
        string descricao = Console.ReadLine();
        Produto produto = produtos.Find(p => p.Descricao.Equals(descricao, StringComparison.OrdinalIgnoreCase));

        if (produto != null)
        {
            Console.Write("Quantidade a ser adicionada: ");
            int quantidade = int.Parse(Console.ReadLine());
            produto.Quantidade += quantidade;
            Console.WriteLine("Entrada de estoque registrada com sucesso!");
        }
        else
        {
            Console.WriteLine("Produto não encontrado.");
        }
    }

    private static void SaidaEstoque()
    {
        Console.Clear();
        Console.Write("Descrição do Produto: ");
        string descricao = Console.ReadLine();
        Produto produto = produtos.Find(p => p.Descricao.Equals(descricao, StringComparison.OrdinalIgnoreCase));

        if (produto != null)
        {
            Console.Write("Quantidade a ser removida: ");
            int quantidade = int.Parse(Console.ReadLine());
            if (quantidade <= produto.Quantidade)
            {
                produto.Quantidade -= quantidade;
                Console.WriteLine("Saída de estoque registrada com sucesso!");
            }
            else
            {
                Console.WriteLine("Quantidade solicitada é maior do que a disponível em estoque.");
            }
        }
        else
        {
            Console.WriteLine("Produto não encontrado.");
        }
    }
}
