/**
 * Plotly Theme Synchronization for MyST Book
 * Automatically updates Plotly plots when the theme changes between light and dark mode
 */

(function() {
  'use strict';

  // Define light and dark theme templates for Plotly
  const lightTemplate = {
    layout: {
      paper_bgcolor: '#ffffff',
      plot_bgcolor: '#f8fafc',
      font: { color: '#1e293b' },
      xaxis: {
        gridcolor: '#e2e8f0',
        linecolor: '#cbd5e1',
        tickcolor: '#64748b',
      },
      yaxis: {
        gridcolor: '#e2e8f0',
        linecolor: '#cbd5e1',
        tickcolor: '#64748b',
      },
    }
  };

  const darkTemplate = {
    layout: {
      paper_bgcolor: '#0f172a',
      plot_bgcolor: '#1e293b',
      font: { color: '#f1f5f9' },
      xaxis: {
        gridcolor: '#334155',
        linecolor: '#475569',
        tickcolor: '#94a3b8',
      },
      yaxis: {
        gridcolor: '#334155',
        linecolor: '#475569',
        tickcolor: '#94a3b8',
      },
    }
  };

  /**
   * Get current theme from document
   */
  function getCurrentTheme() {
    return document.documentElement.classList.contains('dark') ? 'dark' : 'light';
  }

  /**
   * Update all Plotly plots on the page
   */
  function updatePlotlyTheme(theme) {
    const template = theme === 'dark' ? darkTemplate : lightTemplate;
    
    // Find all Plotly divs
    const plotlyDivs = document.querySelectorAll('.plotly-graph-div');
    
    plotlyDivs.forEach(div => {
      if (div && div.data) {
        // Update the layout while preserving existing settings
        const update = {
          paper_bgcolor: template.layout.paper_bgcolor,
          plot_bgcolor: template.layout.plot_bgcolor,
          'font.color': template.layout.font.color,
          'xaxis.gridcolor': template.layout.xaxis.gridcolor,
          'xaxis.linecolor': template.layout.xaxis.linecolor,
          'xaxis.tickcolor': template.layout.xaxis.tickcolor,
          'yaxis.gridcolor': template.layout.yaxis.gridcolor,
          'yaxis.linecolor': template.layout.yaxis.linecolor,
          'yaxis.tickcolor': template.layout.yaxis.tickcolor,
        };
        
        // Handle subplots (xaxis2, yaxis2, etc.)
        if (div.layout) {
          Object.keys(div.layout).forEach(key => {
            if (key.match(/^[xy]axis\d+$/)) {
              const axis = key.startsWith('x') ? 'xaxis' : 'yaxis';
              update[`${key}.gridcolor`] = template.layout[axis].gridcolor;
              update[`${key}.linecolor`] = template.layout[axis].linecolor;
              update[`${key}.tickcolor`] = template.layout[axis].tickcolor;
            }
          });
        }
        
        // Use Plotly.relayout to update without full redraw
        if (window.Plotly) {
          window.Plotly.relayout(div, update);
        }
      }
    });
  }

  /**
   * Initialize theme synchronization
   */
  function initThemeSync() {
    // Update plots on initial load
    const currentTheme = getCurrentTheme();
    updatePlotlyTheme(currentTheme);

    // Watch for theme changes using MutationObserver
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
          const newTheme = getCurrentTheme();
          updatePlotlyTheme(newTheme);
        }
      });
    });

    // Observe changes to the document element's class
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class']
    });

    // Also listen for custom theme change events if they exist
    document.addEventListener('themeChange', (e) => {
      updatePlotlyTheme(e.detail?.theme || getCurrentTheme());
    });
  }

  // Wait for Plotly to be loaded
  function waitForPlotly() {
    if (window.Plotly) {
      initThemeSync();
    } else {
      setTimeout(waitForPlotly, 100);
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', waitForPlotly);
  } else {
    waitForPlotly();
  }
})();
