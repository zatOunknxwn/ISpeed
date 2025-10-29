using System;
using irsdkSharp;

class Program
{
    static void Main()
    {
        using var ir = new irsdkSharp();

        if (ir.startup())
        {
            Console.WriteLine("Подключение к iRacing успешно!");

            // Получаем основные данные
            Console.WriteLine($"Сессия: {ir.SessionInfo.Sessions}");
            Console.WriteLine($"Позиция игрока: {ir.Telemetry.PlayerCarPosition}");
        }
        else
        {
            Console.WriteLine("Не удалось подключиться к iRacing.");
        }

        Console.WriteLine("Нажмите любую клавишу для выхода...");
        Console.ReadKey();
    }
}
