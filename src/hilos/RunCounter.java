/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hilos;

/**
 *
 * @author User
 */
public class RunCounter {
    public static void main(String[] args) {
        var counter = new Counter();
       // Thread hilo = new Thread();
        
   for (var i = 0; i < 10; i++) {
    Thread hilo = new Thread(() -> {
        counter.increment();
        System.out.printf("valor para %s - %d\n",
                Thread.currentThread().getName(),
                counter.getCount());
    });
    hilo.start();
    try {
        hilo.join(); // Esperar a que el hilo termine
    } catch (InterruptedException e) {
        e.printStackTrace();
        }
     }
   
    }
        
}

