
      subroutine rotate_fortran(x, xp, n)

      integer n
      real*8 x(n), xp(n)
      
      real(8),parameter :: PI  = 3.14159265359
      
Cf2py intent(in) n
Cf2py intent(inout) x
Cf2py intent(inout) xp

      integer ii
      real*8 theta, costh, sinth, x_new, xp_new

      do ii=1,n
        theta = PI/3. + 0.01*x(ii)
        costh = cos(theta)
        sinth = sin(theta)
    
        x_new = x(ii)*costh + xp(ii)*sinth
        xp_new = -xp(ii)*sinth + x(ii)*costh

        x(ii) = x_new
        xp(ii) = xp_new
          
      enddo
      end
