using System;
class Program
{
    public static void Main(string[] args)
    {
        int num;
        Console.WriteLine("Digite um numero: ");
        num = int.Parse(Console.ReadLine());
        if (num > 0)
        {
            Console.WriteLine("Número Positivo");
        }
        else
        {
            Console.WriteLine("Número Negativo");
        }
    }
}
