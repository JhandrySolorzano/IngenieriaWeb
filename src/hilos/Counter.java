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
public class Counter {
    private int count;

    public void increment() {
        try {
            Thread.sleep(100);
        } catch (InterruptedException ie) {}
        count ++;
    }

    public int getCount() {
        return count;
    }
}
