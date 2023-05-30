class Main {
    public static void main(String[] args) {
        move(2, "2");
    }
    
    static void move(int distanceInMeters , String name ) {
        int num = 9 ;
        System.out.println ( name + " moved " + distanceInMeters + "m." );
        if ( num < 1 || num > 10 ) {
        System.out.println ( "That is not between 1 and 10");
        }
    }
}